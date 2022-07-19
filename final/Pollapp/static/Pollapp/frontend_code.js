let i = 3;

function addField(){
    if (i <=10){
        const adddelete = document.getElementById("add_and_delete").style.display = "block"
        const answer = document.createElement('div');
        answer.className = "field"
        answer.id = `answer${i}`
        answer.innerHTML = `
        <label class="label">Answer #${i}</label>
        <div class="control">
            <input id="answer_input${i}"class="input" type="text" placeholder="Enter your answer"></input>
        </div>`;
        document.getElementById("answers").append(answer);
        i++;
    }
    else{
        alert("Can't add more answers")
    }
    
}

function removeField(){
    if (i>3){
        i--;
        document.getElementById(`answer${i}`).remove();
        if (i == 3){
            document.getElementById("add_and_delete").style.display = "none";
        }
    }
    
    
}



