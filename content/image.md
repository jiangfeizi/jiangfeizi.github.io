Title: 我的老婆


<script>
function myFunction()
{
    var x=document.getElementById("demo").value;
	if(x=="520")
	{
		element=document.getElementById("img");
        element.src="/images/yang.jpg";
	}
    else
    {
        alert("密码不正确");
    }
}
</script>

<p>请输入密码。</p>
<input id="demo" type="text">
<img id="img" border="0" src="" alt="Pulpit rock" width="304" height="228">
<button type="button" onclick="myFunction()">确认</button>
