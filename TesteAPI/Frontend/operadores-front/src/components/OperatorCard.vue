<template>
<div class="operator-card" @click="$emit('show-details', operator)">
    <div class="card-header">
        <h3>{{ operator.Razao_Social }}</h3>
        <span class="badge">{{ operator.Modalidade }}</span>
    </div>
    
    <div class="card-body">
        <div class="info-row">
            <span class="label">Nome Fantasia: </span>
            <span class="value"> {{ operator.Nome_Fantasia || 'N/A' }}</span>
        </div>
        
        <div class="info-row">
            <span class="label">Localização: </span>
            <span class="value">{{ operator.Cidade }}/{{ operator.UF }}</span>
        </div>
    </div>
</div>
</template>

<script>
export default {
    props: {
        operator: {
            type: Object,
            required: true
        }
    },
    emits: ['show-details']
}
</script>

<style scoped>
.operator-card {
    border: 1px solid var(--medium-gray);
    border-radius: 12px; 
    overflow: hidden;
    transition: all 0.3s ease;
    background: white;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); 
    margin: 0 auto; 
    width: 100%; 
    max-width: 350px; 
}

.operator-card:hover {
    transform: translateY(-3px); 
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    border-color: var(--primary-color);
}

.card-header {
    padding: 18px;
    background: var(--light-gray);
    border-bottom: 1px solid var(--medium-gray);
}

.card-body {
    padding: 18px;
}

@media (max-width: 600px) {
    .operator-card {
        max-width: 100%; 
        border-radius: 10px;
    }

    .card-header,
    .card-body {
        padding: 15px;
    }
}
</style>