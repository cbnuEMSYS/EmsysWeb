var imgs = [
    '/static/img/code-child-contest.jpg', 
    '/static/img/letsgo.jpg', 
    '/static/img/study.jpg'
];
var imgCnts = 0;
var curImg = 0;
var nexImg = 1;

function updateIntroduceImage() {
    var introduceImageCur = document.querySelectorAll('.introduce-board')[curImg];
    var introduceImageUpd = document.querySelectorAll('.introduce-board')[nexImg];


    introduceImageUpd.style.backgroundImage = 'url(' + imgs[imgCnts] + ')';
    introduceImageUpd.classList.add('active');

    introduceImageCur.classList.remove('active');
    imgCnts = (imgCnts+1)%3;
    curImg = (curImg + 1)%2;
    nexImg = (nexImg + 1)%2;
}

updateIntroduceImage();

setInterval(updateIntroduceImage, 5000);

