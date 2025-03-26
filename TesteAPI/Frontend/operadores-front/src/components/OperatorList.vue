<template>
<div class="operator-list">
    <div v-if="loading" class="loading">
    <div class="spinner"></div>
    <span>Carregando resultados...</span>
    </div>
    
    <div v-if="error" class="error">
    <span class="error-icon">⚠️</span>
    {{ error }}
    </div>
    
    <div v-if="operators.length > 0" class="results-info">
    <p>Mostrando {{ operators.length }} resultados</p>
    </div>
    
    <div class="results">
    <OperatorCard
        v-for="operator in operators"
        :key="operator.Registro_ANS"
        :operator="operator"
        @show-details="$emit('show-details', operator)"
    />
    </div>
</div>
</template>

<script>
import OperatorCard from './OperatorCard.vue'

export default {
    components: { OperatorCard },
    props: {
        operators: {
            type: Array,
            default: () => []
        },
        loading: Boolean,
        error: String
    },
    emits: ['show-details']
}
</script>

<style scoped>
.operator-list {
    margin-top: 30px;
}

.loading {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 30px;
    color: var(--secondary-color);
}

.spinner {
    width: 24px;
    height: 24px;
    border: 3px solid rgba(66, 185, 131, 0.2);
    border-radius: 50%;
    border-top-color: var(--primary-color);
    animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.error {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 15px;
    background: #ffebee;
    color: var(--error-color);
    border-radius: 6px;
    margin-bottom: 20px;
}

.error-icon {
    font-size: 20px;
}

.results-info {
    margin-bottom: 20px;
    color: var(--secondary-color);
    font-size: 0.9rem;
}

.results {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}

@media (max-width: 768px) {
    .results {
        grid-template-columns: 1fr;
    }
}
</style>