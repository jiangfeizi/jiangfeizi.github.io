Title: 我的老婆
Date: 2024-10-19

<script>
function myFunction()
{
    var x=document.getElementById("password").value;
	if(x=="951019")
	{
        photos = document.querySelectorAll('.photo img');

        photos.forEach(photo => {
            photo.src = "/images/yang.jpg"
        });
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

<div class="photo-wall">

</div>

<form class="inline-form">
    <input id="password" type="text" placeholder="输入密码">
    <button type="button" onclick="myFunction()">提交</button>
</form>

<div class="photo-wall">
    <div class="photo">
        <img src="" alt="照片1">
    </div>
    <div class="photo">
        <img src="" alt="照片2">
    </div>
    <div class="photo">
        <img src="" alt="照片3">
    </div>
</div>

