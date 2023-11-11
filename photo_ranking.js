document.addEventListener("DOMContentLoaded", function () {
    const photoContainer = document.getElementById("photoContainer");

    fetch('data/data.json')
        .then(response => response.json())
        .then(data => {
            // data.json ファイルから写真の情報を取得
            const photos = Object.keys(data).map(key => ({ id: key, ...data[key], title: data[key].title.trim() || 'デフォルトタイトル' }));

            // 写真を表示するためのHTMLを生成
            const photoHTML = photos.map(photo => `<div class="photo">
                <p class="photo-title">${photo.title}</p>
                <img src="data/${photo.filename}" alt="${photo.title}" style="width: 50%;">
            </div>`).join('');

            // 写真とタイトルをphotoContainerに追加
            photoContainer.innerHTML = `<div class="photo-column">${photoHTML}</div>`;
        })
        .catch(error => console.error("写真の読み込みエラー", error));
});
