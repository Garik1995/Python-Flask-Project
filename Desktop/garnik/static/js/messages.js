new Vue ({
    el: "#chat",
    delimiters: ["[%","%]"],
    data:{
        activeUser: '',
        messageFriend: [],
        messageText: '',
        io: io()
    },
    created(){
        this.activeUser = document.querySelector('.active_chat').getAttribute('data-id')
        this.io.on('connect', ()=> {
    console.log('connected')
        this.io.emit('my event', {data: 'I\'m connected!'});
        this.io.emit('getMessages',{activeUser:this.activeUser})
        this.io.on("getMessages",(data)=>{
            this.messageFriend = JSON.parse(data.messages)
            console.log(this.messageFriend)
        })
    });
//        axios.post('/getMessages', {activeUser:this.activeUser}).then((r)=>{
//            this.messageFriend = r.data
//        })
    },
    methods: {
        chat(e,id){
            let activeChat = document.querySelectorAll('.active_chat')
            this.activeUser = id
            for(let i=0; i<activeChat.length;i++){
                activeChat[i].classList.remove('active_chat')
            }
            e.target.parentElement.parentElement.parentElement.classList.add('active_chat')
//             console.log('ok2')
             axios.post('/getMessages', {activeUser:this.activeUser}).then((r)=>{
                this.messageFriend = r.data
             })
        },
        send(){
            if(this.activeUser!=''){
//                axios.post('/sendMessage',{activeUser:this.activeUser,messageText:this.messageText}).then((r)=>{
//                    this.messageText = ''
//                    this.messageFriend = r.data
//                })
                 this.io.emit('sendMessage', {messageText:this.messageText, activeUser:this.activeUser})
            }

        }
    }
})

