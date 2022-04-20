new Vue ({
    el: "#daa",
    delimiters: ["[%","%]"],
    data:{



    },

        methods:{
            like(id){
                alert(id)
                axios.post("/like",{id:id}).then((r)=>{})

                },


            dislike(id){
               alert(id)
                axios.post("/dislike",{id:id}).then((a)=>{})

                },

},


})
