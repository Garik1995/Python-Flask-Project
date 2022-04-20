new Vue ({
    el: "#app",
    delimiters: ["[%","%]"],
    data:{

        photo:[],

    },
        methods:{

               glavni(a){

                axios.post("/glavni",{id:a}).then((v)=>{

                })

               },

               delet(c){

                    axios.post('/deletePhoto', {id:c}).then((r)=>{
                        this.photo = this.photo.filter((a) => a.id!=c)
                    })


               }

                },


        created(){
            axios.post("/getPhoto").then((r)=>{
            console.log(r.data)
            this.photo = r.data
            })

    },
})
