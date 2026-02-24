//기본
document
  .getElementsByTagName('video')[0]
  .addEventListener('ended', function () {
    console.log('nextPage');
    document.querySelector('#next-btn')?.click();
    if (document.querySelector('.ui-draggable-handle').style.z - index > 0) {
      document.querySelector('.ui-draggable-handle')?.click();
      document.querySelector('#next-btn')?.click();
    }
  });

// 완성본
if (document.querySelector('#quiz')) {
  document.querySelector('.ui-draggable-handle')?.click();
  document.querySelector('#next-btn')?.click();
} else {
  showPlayer();
  if (document.querySelector('#quiz')) {
    document.querySelector('#next-btn')?.click();
  }
  document
    .getElementsByTagName('video')[0]
    .addEventListener('ended', function () {
      document.querySelector('#next-btn')?.click();
    });
}
