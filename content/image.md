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

document.addEventListener('DOMContentLoaded', () => {
    const photos = document.querySelectorAll('.photo img');

    photos.forEach(photo => {
        photo.addEventListener('click', () => {
            const overlay = document.createElement('div');
            overlay.classList.add('overlay');
            overlay.innerHTML = `
                <div class="overlay-content">
                    <img src="${photo.src}" alt="${photo.alt}">
                </div>
            `;
            document.body.appendChild(overlay);

            // 点击关闭
            overlay.addEventListener('click', () => {
                overlay.remove();
            });
        });
    });
});
</script>

<!-- <p>请输入密码。</p>
<input id="demo" type="text">
<img id="img" border="0" src="" alt="Pulpit rock" width="304" height="228">
<button type="button" onclick="myFunction()">确认</button> -->

<div class="photo-wall">
    <div class="photo">
        <img src="/images/yang.jpg" alt="照片1">
    </div>
    <div class="photo">
        <img src="/images/yang.jpg" alt="照片2">
    </div>
    <div class="photo">
        <img src="/images/yang.jpg" alt="照片3">
    </div>
    <!-- 更多照片 -->
</div>

