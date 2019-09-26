const time= document.getElementById('time'),
    greeting = document.getElementById('greeting');

const showAmPm = true;

function showTime() {
    let today = new Date(),
        hour = today.getHours(),
        min = today.getMinutes(),
        sec = today.getSeconds();

    const amPm = hour >= 12 ? 'PM' : 'AM';

    hour = hour %12 || 12;

    time.innerHTML= `${hour}<span>:</span>${addZero(min)}<span>:</span>${addZero(
        sec
    )} ${showAmPm ? amPm : ''}`;

    setTimeout(showTime, 1000);
}

function addZero(n) {
    return (parseInt(n, 10) < 10 ? '0' : '') + n;
}

function setBcGreet() {
    let today = new Date(),
        hour = today.getHours();

    if(hour <12) {
        document.body.style.backgroundImage = "url('../static/2.png')";
        greeting.textContent = 'Good Morning, ';
        document.body.style.color = '#f8fc23';
    } else if(hour<18) {
        document.body.style.backgroundImage = "url('../static/2.png')";
        greeting.textContent = 'Good Afternoon, ';
        document.body.style.color = '#f8fc23';
    } else {
        document.body.style.backgroundImage = "url('../static/2.png')";
        greeting.textContent = 'Good Evening, ';
        document.body.style.color = ' #f8fc23';
    }
}

showTime();
setBcGreet();