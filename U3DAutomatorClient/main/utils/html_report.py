# -*- coding: utf-8 -*-
"""
A TestRunner for use with the Python unit testing framework. It
generates a HTML report to show the result at a glance.

The simplest way to use this is to invoke its main method. E.g.

    import unittest
    import HTMLTestRunner

    ... define your tests ...

    if __name__ == '__main__':
        HTMLTestRunner.main()


For more customization options, instantiates a HTMLTestRunner object.
HTMLTestRunner is a counterpart to unittest's TextTestRunner. E.g.

    # output to a file
    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test
    runner.run(my_test_suite)


------------------------------------------------------------------------
Copyright (c) 2004-2007, Wai Yip Tung
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name Wai Yip Tung nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# URL: http://tungwaiyip.info/software/HTMLTestRunner.html
from unittest.runner import _WritelnDecorator
import os
import shutil
from main.object.enum import Platform, Environment

__author__ = "Wai Yip Tung"
__version__ = "0.8.2"

"""
Change History

Version 0.8.2
* Show output inline instead of popup window (Viorel Lupu).

Version in 0.8.1
* Validated XHTML (Wolfgang Borgert).
* Added description of test classes and test cases.

Version in 0.8.0
* Define Template_mixin class for customization.
* Workaround a IE 6 bug that it does not treat <script> block as CDATA.

Version in 0.7.1
* Back port to Python 2.3 (Frank Horowitz).
* Fix missing scroll bars in detail log (Podi).
"""
# coding=utf-8
# TODO: color stderr
# TODO: simplify javascript using ,ore than 1 class in the class attribute?
import datetime
import StringIO
import sys
import unittest
from xml.sax import saxutils
from main.log.logger import get_logger
import socket
from script.windows.PPT3DSetting import DataBaseSet
from main.utils.path import Path
import time
from main.sender.im import SendNew99U

# ------------------------------------------------------------------------
# The redirectors below are used to capture output during testing. Output
# sent to sys.stdout and sys.stderr are automatically captured. However
# in some cases sys.stdout is already cached before HTMLTestRunner is
# invoked (e.g. calling logging.basicConfig). In order to capture those
# output, use the redirectors for the cached stream.
#
# e.g.
#   >>> logging.basicConfig(stream=HTMLTestRunner.stdout_redirector)
#   >>>

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


# ----------------------------------------------------------------------
# Template

class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.

    Overall structure of an HTML report

    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: 'pass',
        1: 'fail',
        2: 'error',
    }

    DEFAULT_TITLE = 'Unit Test Report'
    DEFAULT_DESCRIPTION = ''

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<?xml get_version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%s</title>
    <meta name="generator" content="%s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    %s
</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

%s
%s
%s

</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending)


    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { }

/* -- heading ---------------------------------------------------------------------- */
h1 {
	font-size: 16pt;
	color: gray;
}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
}
#result_table {
    width: 80%;
    border-collapse: collapse;
    border: 1px solid #777;
}
#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
}
#result_table td {
    border: 1px solid #777;
    padding: 2px;
}
#total_row  { font-weight: bold; }
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """<div class='heading'>
<h1>%(title)s</h1>
%(parameters)s
<p class='description'>%(description)s</p>
</div>

"""  # variables: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s:</strong> %(value)s</p>
"""  # variables: (name, value)

    # ------------------------------------------------------------------------
    # Report
    #

    REPORT_TMPL = """
<p id='show_detail_line'>Show
<a href='javascript:showCase(0)'>Summary</a>
<a href='javascript:showCase(1)'>Failed</a>
<a href='javascript:showCase(2)'>All</a>
</p>
<table id='result_table'>
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row'>
    <td>Test Group/Test case</td>
    <td>spendtime</td>
    <td>Count</td>
    <td>Pass</td>
    <td>Fail</td>
    <td>Error</td>
    <td>View</td>
    
</tr>
%(test_list)s
<tr id='total_row'>
    <td>Total</td>
    <td>spendtime</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td>&nbsp;</td>
    
</tr>
</table>
"""  # variables: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>spendtime</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">Detail</a></td>
    
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'><img src='%(ima_path)s' width="700" height="450"></div></td>
    <td class='%(style)s'><div class='testcase'>%(spendtime)s</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
        %(status)s</a>

    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        %(script)s
        </pre>
    </div>
    <!--css div popup end-->

    </td>
    
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'><img src='%(ima_path)s' width="700" height="450"></div></td>
    
    <td class='%(style)s'><div class='testcase'>%(spendtime)s</div></td>
    <td colspan='5' align='center'>%(status)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #

    ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""


# -------------------- The end of the Template class -------------------


TestResult = unittest.TextTestResult


class NewTestResult(TestResult):
    # note: NewTestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.
    def __init__(self, stream=sys.stderr, descriptions=None, verbosity=2):
        TestResult.__init__(self, _WritelnDecorator(stream), descriptions, verbosity)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.s_time = 0
        self.e_time = 0
        self.spend_time = 0
        self.times = []
        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = StringIO.StringIO()
        # stdout_redirector.fp = self.outputBuffer
        # stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        self.s_time = datetime.datetime.now()
        # sys.stdout = stdout_redirector
        # sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()
        self.spendTime()

    def spendTime(self):
        self.e_time = datetime.datetime.now()
        self.spend_time = self.e_time - self.s_time

        # #print "本脚本运行时间：", self.spend_time
        return self.spend_time

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        st = self.spendTime()
        self.result.append((0, test, output, '', st))
        if self.verbosity > 1:
            get_logger().info("%s ... ok" % str(test))
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        st = self.spendTime()
        # print "errortest:", test, "output:", output, "_exc_str:", _exc_str, "str:", str
        self.result.append((2, test, output, _exc_str, st))
        if self.verbosity > 1:
            get_logger().info("%s ...Error" % str(test))
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        st = self.spendTime()
        # print "failuretest:", test, "output:", output, "_exc_str:", _exc_str, "str:", str
        self.result.append((1, test, output, _exc_str, st))
        if self.verbosity > 1:
            get_logger().info("%s ... Failure" % str(test))
        else:
            sys.stderr.write('F')


class HTMLTestRunner(Template_mixin):
    """
    """
    def __init__(self, stream=sys.stdout, verbosity=2, title=None, description=None):

        self.TestCaseNames = ''
        self.Pass = 0
        self.Fail = 0
        self.Error = 0
        self.Detail = ""
        self.task_id = 0
        self.ip = ""
        self.IP_id=0
        self.stream = stream
        self.dirname = self.stream.name.split("\\")[-1].split(".")[0]
        # #print "报告名称2：", self.dirname
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            try:
                self.title = title.decode('utf8')
            except :
                self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

    def run(self, test):

        "Run the given test case or test suite."
        result = NewTestResult(stream=sys.stderr, descriptions=self.description, verbosity=self.verbosity)
        test(result)
        self.stopTime = datetime.datetime.now()

        self.generateReport(test, result)
        result.printErrors()
        print >> sys.stderr, "-" * 70
        print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime - self.startTime)
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e, st in result_list:
            cls = t.__class__
            if not rmap.has_key(cls):
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e, st))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []
        if result.success_count: status.append('Pass %s' % result.success_count)
        if result.failure_count: status.append('Failure %s' % result.failure_count)
        if result.error_count:   status.append('Error %s' % result.error_count)
        if status:
            status = ' '.join(status)
        else:
            status = 'none'
        get_logger().info("Start Time: %s" % startTime)
        get_logger().info("Duration: %s" % duration)
        get_logger().info("Status: %s" % status)
        return [
            ('Start Time', startTime),
            ('Duration', duration),
            ('Status', status),
        ]

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'HTMLTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)

        # 用例列表
        caseNames = []
        for cid, (cls, cls_results) in enumerate(self.sortResult(result.result)):
            caseNames.append(cls.__name__)
        self.TestCaseNames = ','.join(caseNames)
        self.Pass = result.success_count
        self.Fail = result.failure_count
        self.Error = result.error_count
        # 数据库操作
        #
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            self.ip = s.getsockname()[0]
        finally:
            s.close()
        d = DataBaseSet.DataBase()
        sql_ip = "select IP_id from t_IPs where ip='" + self.ip + "'"
        self.IP_id = d.getData(sql_ip)

        # 获取任务IDDataBaseSet.DataBase()
        # sql_lastId = "SHOW TABLE STATUS where Name = 't_Result'"
        # d = DataBaseSet.DataBase()
        # self.task_id = d.getData(sql_lastId)
        self.task_id = os.getenv(Environment.Result_id)
        #print "task_id:", self.task_id
        try:
            sql = "Update t_Result as R Set R.StartTime='%s', R.StopTime='%s', R.Duration='%s', R.TestCaseName='%s'," \
                  " R.Total='%d', R.Pass='%d', R.Fail='%d', R.Error='%d', R.IP='%d' where R.Result_id='%d'" \
                  % (self.startTime, self.stopTime,self.stopTime - self.startTime, self.TestCaseNames,
                     self.Pass + self.Fail + self.Error, self.Pass, self.Fail, self.Error, self.IP_id[0],int(self.task_id)-1)
            d.databaseOperate(sql)
        except:
            #print "更新t_Result失败"
            pass

        report = self._generate_report(result)
        ending = self._generate_ending()

        output = self.HTML_TMPL % (
            saxutils.escape(self.title),
            generator,
            stylesheet,
            heading,
            report,
            ending,
        )
        # 数据库操作
        # #print "html_report  3"
        # sql_resultID = "Update t_Performance as P, t_Result as R SET P.Result_id = R.Result_id where P.Time > R.StartTime and P.Time < R.StopTime and P.Time > '%s' and P.Time < '%s' and P.IP_id = %d" %(self.startTime, self.stopTime, self.IP_id[0])
        #
        # d.databaseOperate(sql_resultID)
        # # #print "html_report  4"

        try:
            self.stream.write(output.encode('utf8'))
        except:
            self.stream.write(output.decode('gbk').encode('utf8'))

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                name=saxutils.escape(name),
                value=saxutils.escape(value),
            )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
        )
        return heading

    def _generate_report(self, result):

        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = 0
            for n, t, o, e, st in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                else:
                    ne += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name

            #caseNames.append(cls.__name__)
            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc=desc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid + 1),
            )
            #print "desc:", cls.__name__ , "count:", np + nf + ne, "Pass:", np, "fail:", nf, "error:", ne

            rows.append(row)
            #caseNames.append(cls.__name__)
            for tid, (n, t, o, e, st) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e, st, cls.__name__)

            r = ''
            if np == 1:
                r += "Pass "
            elif nf == 1 :
                r += "Fail "
            else:
                r += "Error"

            # 数据库操作
            # 获取用例id
            try:
                sql = "SELECT Name_id from t_CaseName where TestCaseName = '" + cls.__name__ + "'"
                d = DataBaseSet.DataBase()
                name_id = d.getData(sql)

                #### sql_resultID = "Update t_Performance as P, t_Result as R SET P.Result = '%s', P.Detail = '%s' where P.Time > '%s' and P.Time < '%s' and P.Name_id = '%s' and P.IP_id = '%d'" %(r, self.Detail, self.startTime,self.stopTime, name_id[0], )
                # 详细结果输出
                # self.Detail = self.Detail.replace("\\", "\\\\")  # 反斜杠
                # self.Detail = self.Detail.replace("'", "\\\'")  # 详细内容中的转义
                # #print "r:", r, "startTime:", self.startTime, "stopTime:", self.stopTime, "name_id:", name_id[0]
                # sql_resultID = "Update t_Performance as P, t_Result as R SET P.Result = '%s' where P.Time > '%s' and P.Time < '%s' and P.Name_id = '%s' and P.IP_id = '%s'" % (r, self.startTime,self.stopTime, name_id[0], self.IP_id[0])
                # sql_casetest= "Insert into t_CaseTest (Name_id, Create_Time, Result, Result_id, Detail) values(%d,'%s','%s',%d, '%s')" % (name_id[0], datetime.datetime.now(), r, int(self.task_id)-1, e)
                sql_casetest= "Insert into t_CaseTest (Name_id, Create_Time, Result, Result_id) values(%d,'%s','%s',%d)" % (name_id[0], datetime.datetime.now(), r, int(self.task_id)-1)

                # d.databaseOperate(sql_resultID)
                d.databaseOperate(sql_casetest)
            except:
                #print "数据库t_CaseTest操作失败"
                pass


        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
        )
        return report

    def _generate_report_test(self, rows, cid, tid, n, t, o, e, st, script_name):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            #  some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            # uo = o.decode('latin-1')
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            #  some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            # ue=e.decode("latin-1")
            ue = e
        else:
            ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )
        # #print "detail", script
        self.Detail = script
        testImagPath = os.getcwd() + ur"\report\windows\screenshoot"   # 保存截图到新建文件夹
        Path.create_file(testImagPath)
        newPath = os.getcwd() + ur"\report\windows" + "\\" + self.dirname
        self.copyImage(testImagPath, newPath)
        ima=self.dirname + "\\" + script_name + ".png"
        #print "_script_name_", script_name
        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'none'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
            ima_path=ima,
            spendtime=st,
        )
        rows.append(row)

        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL

    def copyImage(self, path, newPath):
        if os.path.exists(newPath):
            pass
        else:
            os.mkdir(newPath)
        alllist = os.listdir(path + "\\")
        for i in alllist:
            aa, bb = i.split(".")
            oldname = path + "\\" + aa + "." + bb
            newname = newPath + "\\" + aa + "." + bb
            shutil.copyfile(oldname, newname)
        shutil.rmtree(path)
        os.mkdir(path)

##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
