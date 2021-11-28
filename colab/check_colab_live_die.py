
'''
function check_connect(){
    let connect = document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect-icon")
    if(connect){
        console.log("Live")
    }
    else{
        console.log("Die")
    }
}
setInterval(check_connect, 3000)
'''
