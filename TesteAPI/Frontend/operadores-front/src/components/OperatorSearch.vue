<template>
<div class="operator-search">
    <h1>Busca de Operadoras de Saúde</h1>
    <div class="search-box">
        <input
            type="text"
            v-model="searchQuery"
            @input="debounceSearch"
            placeholder="Digite para buscar..."
        />
        <button @click="handleSearch">Buscar</button>
    </div>
</div>
</template>

<script>
import { ref } from 'vue'

export default {
    emits: ['search'],
    setup(props, { emit }) {
        const searchQuery = ref('')
        let debounceTimer = null
    
        const debounceSearch = () => {
            clearTimeout(debounceTimer)
            debounceTimer = setTimeout(() => {
            handleSearch()
            }, 500)
        }
    
        const handleSearch = () => {
            emit('search', searchQuery.value)
        }
    
        return {
            searchQuery,
            debounceSearch,
            handleSearch
        }
    }
}
</script>

<style scoped>
.operator-search {
    margin-bottom: 30px;
    text-align: center;
}

.operator-search h1 {
    color: var(--secondary-color);
    margin-bottom: 20px;
    font-size: 2rem;
}

.search-box {
    display: flex;
    max-width: 600px;
    margin: 0 auto;
    gap: 10px;
}

.search-box input {
    flex: 1;
    padding: 12px 15px;
    font-size: 1rem;
    border: 2px solid var(--medium-gray);
    border-radius: 6px;
    transition: all 0.3s ease;
}

.search-box input:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.2);
}

.search-box button {
    padding: 12px 25px;
    background: var(--primary-color);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.3s;
}

.search-box button:hover {
    background: #3aa876;
}

@media (max-width: 600px) {
    .operator-search h1 {
        font-size: 1.5rem;
    }
    
    .search-box {
        flex-direction: column;
    }
}
</style>