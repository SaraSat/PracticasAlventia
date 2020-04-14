<template>
    <div>
        <br><br>
        <input type="checkbox" name="" id="" v-bind:checked='checked' v-on:change="$emit('change',$event.target.checked)">
        <span> {{texto}}</span>
    </div>
</template>
<script>
export default {
    name:'Lista',
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