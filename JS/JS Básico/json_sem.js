let name = "Max Verstappen"
let teams = ["Toro Rosso", "Red Bull Racing"]
let teamsAge = [16, 20]
let age = 28

generateBio(name, teams, teamsAge, age)

//vai pegar todos os dados
function generateBio(name, teams, teamsAge, age){
    console.log(`o nome dele é ${name}`)
    console.log(`a idade dele é ${age}`)
    console.log(`as equipes dele é ${teams}`)
    console.log(`a idade nele nas equipes é ${teamsAge}`)
}


