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

    <div class="filter-row">
      <select v-model="filters.uf" @change="updateCityOptions">
        <option value="">Todos os Estados</option>
        <option v-for="uf in ufOptions" :value="uf">{{ uf }}</option>
      </select>

      <select v-model="filters.cidade" :disabled="!filters.uf">
        <option value="">Todas as Cidades</option>
        <option v-for="city in cityOptions" :value="city">{{ city }}</option>
      </select>

      <select v-model="filters.modalidade">
        <option value="">Todas as Modalidades</option>
        <option v-for="mod in modalityOptions" :value="mod">{{ mod }}</option>
      </select>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { searchOperators, searchFilterOptions } from '@/composables/useOperators'

export default {
  emits: ['search'],
  setup(props, { emit }) {
    const searchQuery = ref('')
    const { operators, loading, error, totalResults, search } = searchOperators()
    
    const { 
      filterOptions, 
      fetchFilterOptions, 
      fetchAllFilters 
    } = searchFilterOptions()
    
    const filters = ref({
      uf: '',
      cidade: '',
      modalidade: ''
    })

    const ufOptions = computed(() => filterOptions.value.uf || [])
    const cityOptions = computed(() => filterOptions.value.cidade || [])
    const modalityOptions = computed(() => filterOptions.value.modalidade || [])
    
    let debounceTimer = null

    // Carrega as opções de cidades quando o estado é selecionado
    const updateCityOptions = async () => {
      filters.value.cidade = ''
      if (filters.value.uf) {
        await fetchFilterOptions('cidade', filters.value.uf)
      }
    }

    // Debounce
    const debounceSearch = () => {
      clearTimeout(debounceTimer)
      debounceTimer = setTimeout(() => {
        handleSearch()
      }, 500)
    }

    const handleSearch = async () => {
      const searchParams = {
        search_term: searchQuery.value,
        uf: filters.value.uf,
        cidade: filters.value.cidade,
        modalidade: filters.value.modalidade
      }
      
      Object.keys(searchParams).forEach(key => {
        if (searchParams[key] === '') {
          delete searchParams[key]
        }
      })
      
      emit('search', searchParams) 
    }

    // Carrega filtros ao montar o componente
    onMounted(async () => {
      await fetchAllFilters()
    })

    return {
      // Search
      searchQuery,
      operators,
      loading,
      error,
      totalResults,
      
      // Filters
      filters,
      ufOptions,
      cityOptions,
      modalityOptions,
      
      // Methods
      debounceSearch,
      handleSearch,
      updateCityOptions
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
  max-width: 700px;
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

.filter-row {
  display: flex;
  gap: 10px;
  justify-content: center;
  max-width: 600px;
  margin: 20px auto 0;
}

.filter-row select {
  flex: 1;
  padding: 12px 15px;
  font-size: 1rem;
  border: 2px solid var(--medium-gray);
  border-radius: 6px;
  background-color: white;
  transition: all 0.3s ease;
}

.filter-row select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.2);
}

@media (max-width: 600px) {
  .operator-search h1 {
    font-size: 1.5rem;
  }
  
  .search-box,
  .filter-row {
    flex-direction: column;
  }
}
</style>