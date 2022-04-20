new Vue ({
    el: "#nots",
    delimiters: ["[%","%]"],
    data:{

        add:"",


    },
        methods:{

                accept(id){

                    axios.post("/accept",{id:id}).then((a)=>{

                })

                },
                delet(id){

                    axios.post("/delete",{id:id}).then((a)=>{

                })

                },
        },


})
