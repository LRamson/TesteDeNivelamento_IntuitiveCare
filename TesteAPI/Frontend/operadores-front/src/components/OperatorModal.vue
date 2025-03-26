<template>
<div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
        <button class="close-modal" @click="$emit('close')">×</button>
        <h2>{{ operator.Razao_Social }}</h2>
        
        <div class="modal-details">
            <div v-for="(value, key) in operator" :key="key" class="detail-row">
                <span class="detail-label">{{ formatKey(key) }}:</span>
                <span class="detail-value">{{ formatValue(key, value) }}</span>
            </div>
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
    emits: ['close'],
    methods: {
        formatKey(key) {
            const map = {
                'Registro_ANS': 'Registro ANS',
                'Razao_Social': 'Razão Social',
                'Nome_Fantasia': 'Nome Fantasia',
                'Endereco_eletronico': 'Email',
                'Data_Registro_ANS': 'Data de Registro',
                'Regiao_de_Comercializacao': 'Região de Comercialização',
                'Cargo_Representante': 'Cargo do Representante'
            };
            return map[key] || key.replace(/_/g, ' ');
        },
        formatValue(key, value) {
            if (value === null || value === undefined) return 'N/A'
            if (key === 'CNPJ') return this.formatCNPJ(value)
            if (key === 'Telefone') return this.formatPhone(this.operator.DDD, value)
            if (key === 'Data_Registro_ANS') return this.formatDate(value)
            return value
        },
        formatCNPJ(cnpj) {
            if (!cnpj) return 'N/A';

            const str = cnpj.toString().padStart(14, '0');

            return `${str.slice(0, 2)}.${str.slice(2, 5)}.${str.slice(5, 8)}/${str.slice(8, 12)}-${str.slice(12)}`;
        },
        formatPhone(ddd, number) {
            if (!number) return 'N/A';

            const numStr = number.toString().replace(/\D/g, '');
            const formatted = numStr.length > 8 
                ? `${numStr.slice(0, numStr.length-4)}-${numStr.slice(numStr.length-4)}`
                : numStr;

            return ddd ? `(${ddd}) ${formatted}` : formatted;
        },
        formatDate(dateStr) {
            if (!dateStr) return 'N/A';

            const date = new Date(dateStr);

            return date.toLocaleDateString('pt-BR');
        }
    }
}
</script>

<style scoped>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    padding: 20px;
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.modal-content {
    background: white;
    border-radius: 8px;
    width: 100%;
    max-width: 800px;
    max-height: 80vh;
    overflow-y: auto;
    padding: 25px;
    position: relative;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.close-modal {
    position: absolute;
    top: 15px;
    right: 15px;
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: var(--dark-gray);
    transition: color 0.3s;
}

.close-modal:hover {
    color: var(--primary-color);
}

.modal-content h2 {
    color: var(--secondary-color);
    margin-bottom: 20px;
    padding-right: 30px;
}

.modal-details {
    margin-top: 20px;
}

.detail-row {
    display: flex;
    margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--light-gray);
}

.detail-row:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

.detail-label {
    font-weight: bold;
    min-width: 200px;
    color: var(--secondary-color);
}

.detail-value {
    flex: 1;
    word-break: break-word;
}

@media (max-width: 768px) {
    .detail-row {
        flex-direction: column;
        gap: 5px;
    }
    
    .detail-label {
        min-width: auto;
    }
    
    .modal-content {
        padding: 20px 15px;
    }
}
</style>