let i = 3;

function addField(){
    if (i <=10){
        const answer = document.createElement('div');
        answer.className = "field"
        answer.innerHTML = `
        <label class="label">Answer #${i}</label>
        <div class="control">
            <input id="answer${i}"class="input" type="text" placeholder="Enter your answer"></input>
        </div>`;
        document.getElementById("answers").append(answer);
        i++;
    }
    else{
        alert("Can't add more answers")
    }
    
}



