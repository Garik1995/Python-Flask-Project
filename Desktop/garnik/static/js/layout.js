new Vue ({
    el: "#search",
    delimiters: ["[%","%]"],
    data:{

        search:"",
        se:[],
    },
        methods:{

            serch(){
                if (this.search == ""){
                    this.se = []
                } else {
               axios.post("/serch",{search:this.search}).then((r)=>{
                   this.se = r.data


                })


                }

                },

                add(id){

                axios.post("/add",{id:id}).then((a)=>{

                })

                },

                del(id){



                },



                },



})
