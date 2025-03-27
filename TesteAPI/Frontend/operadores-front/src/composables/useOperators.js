import { ref } from 'vue'

export function searchOperators() {
    const operators = ref([])
    const loading = ref(false)
    const error = ref(null)
    const totalResults = ref(0)

    const search = async (searchParams) => {
        loading.value = true
        error.value = null  

        try {
            const queryString = new URLSearchParams()
            for (const [key, value] of Object.entries(searchParams)) {
                if (value !== undefined && value !== '' && value !== null) {
                    queryString.append(key, String(value))
                }
            }

            const response = await fetch(`http://127.0.0.1:5000/api/operators/search?${queryString}`)
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }

            const data = await response.json()
            
            operators.value = data.results
            totalResults.value = data.total
            
        } catch (err) {
            error.value = 'Falha ao buscar operadoras. Tente novamente.'
            console.error('Search error:', err)
        } finally {
            loading.value = false
        }
    }

    return { operators, loading, error, totalResults, search }
}

export function searchFilterOptions() {
    const filterOptions = ref({
        uf: [],
        cidade: [],
        modalidade: []
    })
    const loading = ref(false)
    const error = ref(null)

    const fetchFilterOptions = async (field, uf) => {
        loading.value = true
        error.value = null

        try {
            let url = `http://127.0.0.1:5000/api/operators/filters/${field}`
            if (uf && field === 'cidade') {
                url += `?uf=${encodeURIComponent(uf)}`
            }

            const response = await fetch(url)
            
            if (!response.ok) {
                throw new Error(`Failed to fetch ${field} options`)
            }

            const data = await response.json()
            filterOptions.value[field] = data.values
            
            return data.values
        } catch (err) {
            error.value = `Error loading ${field} options`
            console.error(`Failed to fetch ${field}:`, err)
            return []
        } finally {
            loading.value = false
        }
    }

    const fetchAllFilters = async () => {
        try {
            const [ufs, mods] = await Promise.all([
                fetchFilterOptions('uf'),
                fetchFilterOptions('modalidade')
            ])
            return { ufs, mods }
        } catch (err) {
            console.error('Failed to load initial filters:', err)
            return { ufs: [], mods: [] }
        }
    }

    return {
        filterOptions,
        loading,
        error,
        fetchFilterOptions,
        fetchAllFilters
    }
}