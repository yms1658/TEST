<html>
<head>
<title>PRA4.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #0033b3;}
.s1 { color: #080808;}
.s2 { color: #008080; font-weight: bold;}
.s3 { color: #1750eb;}
</style>
</head>
<body bgcolor="#ffffff">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#c0c0c0" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
PRA4.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">datetime</span>
<span class="s1">a = int(input(</span><span class="s2">&quot;请输入出生年份:&quot;</span><span class="s1">))</span>
<span class="s1">c = int(input(</span><span class="s2">&quot;请输入出生月份:&quot;</span><span class="s1">))</span>
<span class="s1">d = int(input(</span><span class="s2">&quot;请输入出生日:&quot;</span><span class="s1">))</span>
<span class="s1">x = datetime.date.today()</span>
<span class="s1">y = datetime.date(a, c, d)</span>
<span class="s0">if </span><span class="s1">datetime.date.today().month&lt;c:</span>
   <span class="s1">print(</span><span class="s2">&quot;距离下一次生日还有：&quot;</span><span class="s1">+str((datetime.date(datetime.date.today().year,c,d)-x).days)+</span><span class="s2">&quot;天&quot;</span><span class="s1">)</span>
<span class="s0">elif </span><span class="s1">datetime.date.today().month==c </span><span class="s0">and </span><span class="s1">datetime.date.today().day&gt;d:</span>
   <span class="s1">print(</span><span class="s2">&quot;距离下一次生日还有：&quot;</span><span class="s1">+str((datetime.date(datetime.date.today().year+</span><span class="s3">1</span><span class="s1">,c,d)-x).days)+</span><span class="s2">&quot;天&quot;</span><span class="s1">)</span>
<span class="s0">elif </span><span class="s1">datetime.date.today().month==c </span><span class="s0">and </span><span class="s1">datetime.date.today().day&lt;d:</span>
   <span class="s1">print(</span><span class="s2">&quot;距离下一次生日还有：&quot; </span><span class="s1">+ str((datetime.date(datetime.date.today().year,c,d)-x).days) +</span><span class="s2">&quot;天&quot;</span><span class="s1">)</span>
<span class="s0">else </span><span class="s1">:</span>
   <span class="s1">print(</span><span class="s2">&quot;距离下一次生日还有：&quot;</span><span class="s1">+str((datetime.date(datetime.date.today().year+</span><span class="s3">1</span><span class="s1">,c,d)-x).days)+</span><span class="s2">&quot;天&quot;</span><span class="s1">)</span>





</pre>
</body>
</html>