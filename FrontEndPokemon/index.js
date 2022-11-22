const fetchAsync = async (index) => {
    const rawData = await fetch(`http://127.0.0.1:8000/pokemon/${index}`);
    console.log(rawData);
    const pokemonData = await rawData.json();
    console.log(pokemonData);

    const pokemonName = pokemonData.name;
    const nameHeading = document.getElementById('pokemonName');
    nameHeading.textContent = pokemonName;

    const pokeImageFront = document.getElementById('pokeImageFront');
    pokeImageFront.src = pokemonData.frontImg;

    const pokeList = document.getElementById('list');
    pokeList.innerHTML = "";
    for(let i=0; i<3; i++){
        let li = document.createElement('li');
        li.textContent = pokemonData.moves[i];
        pokeList.appendChild(li);
    }
}

const deleteAsync = async (index) => {
    const result = await fetch(`http://127.0.0.1:8000/pokemon/${index}`, { method: 'DELETE' })
    if (result) {
        const nameHeading = document.getElementById('pokemonName');
        nameHeading.textContent = "Pokemon Deleted";
        const pokeList = document.getElementById('list');
        pokeList.innerHTML = "";
        const pokeImageFront = document.getElementById('pokeImageFront');
        pokeImageFront.src = "https://i.pinimg.com/736x/28/97/ec/2897ec5d34936e14686134a874435197.jpg";
    }
}

let index = 1;
fetchAsync(index).catch(err => console.log(err))

const buttonNext = document.getElementById('nextPokemon');
buttonNext.addEventListener('click', () =>{
    index++;
    console.log("index", index);
    // if (index == 5) {
    //     index = 1;
    // }
    fetchAsync(index).catch(err => {
        index = 0;
        console.log(err)
    })
})

const buttonDelete = document.getElementById('deletePokemon');
buttonDelete.addEventListener('click', () =>{
    console.log("delete clicked");
    deleteAsync(index).catch(err => {
        console.log(err)
    })
})

// Simple POST request with a JSON body using fetch
const form = document.querySelector('form');
form.addEventListener('submit', (e) =>{
    e.preventDefault();
    console.log("form submitted");
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
                name: document.getElementById("pname").value, 
                frontImg: document.getElementById("sprite").value, 
                moves: [document.getElementById("move1").value, 
                    document.getElementById("move2").value, 
                    document.getElementById("move3").value]  
            
        })
    };
    fetch('http://127.0.0.1:8000/pokemon', requestOptions)
        .then(response => response.json())
        .then(pokemonData => {
            console.log(pokemonData);

            const pokemonName = pokemonData.name;
            const nameHeading = document.getElementById('pokemonName');
            nameHeading.textContent = pokemonName;

            const pokeImageFront = document.getElementById('pokeImageFront');
            pokeImageFront.src = pokemonData.frontImg;

            const pokeList = document.getElementById('list');
            pokeList.innerHTML = "";
            for(let i=0; i<3; i++){
                let li = document.createElement('li');
                li.textContent = pokemonData.moves[i];
                pokeList.appendChild(li);
            }
        });
})
