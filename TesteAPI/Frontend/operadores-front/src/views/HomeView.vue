<template>
    <div class="app-container">
        <div class="content-wrapper">
            <OperatorSearch @search="handleSearch" />
            <div class="cards-container">
                <OperatorList 
                :operators="operators" 
                :loading="loading" 
                :error="error"
                @show-details="showDetails"
                />
            </div>
            <OperatorModal 
                v-if="showModal" 
                :operator="selectedOperator"
                @close="closeModal"
            />
        </div>
    </div>
</template>
  


<script>
import { ref } from 'vue'
import OperatorSearch from '@/components/OperatorSearch.vue'
import OperatorList from '@/components/OperatorList.vue'
import OperatorModal from '@/components/OperatorModal.vue'
import { searchOperators } from '@/composables/useOperators'

export default {
    components: { OperatorSearch, OperatorList, OperatorModal },
    setup() {
        const { operators, loading, error, search } = searchOperators()
        const showModal = ref(false)
        const selectedOperator = ref(null)

        const handleSearch = (query) => {
            search(query)
        }

        const showDetails = (operator) => {
            selectedOperator.value = operator
            showModal.value = true
        }

        const closeModal = () => {
            showModal.value = false
        }

        return {
            operators,
            loading,
            error,
            handleSearch,
            showDetails,
            showModal,
            selectedOperator,
            closeModal
        }
    }
}
</script>

<style scoped>
.app-container {
    width: 100%;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    padding: 20px;
    background-color: #f5f7fa;
}

.content-wrapper {
    width: 100%;
    max-width: 1200px;
}

.cards-container {
    margin-top: 30px;
    padding: 0 20px; /* Add horizontal padding */
}
</style>