import { ref } from 'vue'

export function searchOperators() {
    const operators = ref([])
    const loading = ref(false)
    const error = ref(null)

    const search = async (query) => {
        if (!query.trim()) {
            operators.value = []
            return
        }

        loading.value = true
        error.value = null

        try {
            const response = await fetch(`http://localhost:5000/api/search?q=${encodeURIComponent(query)}`)
            if (!response.ok) throw new Error('Erro na busca')
            operators.value = await response.json()
        } catch (err) {
            error.value = 'Falha ao buscar operadoras. Tente novamente.'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    return { operators, loading, error, search }
}