let i = 3;

function addField(){
    if (i <=10){
        const adddelete = document.getElementById("add_and_delete").style.display = "block";
        const answer = document.createElement('div');
        answer.className = "field show_animation";
        answer.id = `answer${i}`;
        answer.innerHTML = `
        <label class="label">Answer #${i}</label>
        <div class="control">
            <input class="input" type="text"  name="answer${i}_name" placeholder="Enter your answer"></input>
        </div>`;
        document.getElementById("answers").append(answer);
        const option = document.getElementById(`answer${i}`);
        option.style.animationPlayState = 'running';
        option.addEventListener('animationend', () => {
            option.style.animationPlayState = 'paused';
        });
        i++;
    }
    else{
        alert("Can't add more answers")
    }
    
}

function removeField(){
    if (i>3){
        i--;
        const option = document.getElementById(`answer${i}`);
        option.className = 'field disappear_animation';
        option.style.animationPlayState = 'running';
        option.addEventListener('animationend', () => {
            option.remove();
        });
        
        if (i == 3){
            document.getElementById("add_and_delete").style.display = "none";
        }
    }
    
    
}



