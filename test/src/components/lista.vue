     <template>

        <div class="lista">
            <input type="checkbox" v-bind:checked='checked' v-on:change="$emit('change',$event.target.checked)" >

            <span>

                {{texto}}
            </span>
    
        </div>

    </template>

<script>
export default {
    name:'lista',
    model:{
    prop:'checked',
    event:'change'
    },
    props:{
        id:{type:Number},
        texto:{type:String},
        comprado:{type:Boolean},
        checked:Boolean
    },

}
</script>

