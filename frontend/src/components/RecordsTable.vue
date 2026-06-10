<script setup>
defineProps({
    records: {
        type: Array,
        required: true,
    },
    total: {
        type: Number,
        required: true,
    },
    start: {
        type: String,
        required: true,
    },
    end: {
        type: String,
        required: true,
    },
});
</script>

<template>
    <div class="w-full overflow-x-auto">
        <p class="text-gray-500 text-sm mb-2">
            Almuerzos registrados entre {{ start }} y {{ end }}: {{ total }}
        </p>

        <table class="w-full text-left border-collapse">
            <thead>
                <tr class="bg-gray-100 text-gray-600 text-sm uppercase">
                    <th class="px-4 py-3">ID</th>
                    <th class="px-4 py-3">Nombres</th>
                    <th class="px-4 py-3">Apellidos</th>
                    <th class="px-4 py-3">Fecha</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="records.length === 0">
                    <td colspan="4" class="px-4 py-6 text-center text-gray-400">
                        No hay registros para este período
                    </td>
                </tr>
                <tr
                    v-for="record in records"
                    :key="record.colegio_id + record.registro"
                    class="border-t hover:bg-gray-50"
                >
                    <td class="px-4 py-3">{{ record.colegio_id }}</td>
                    <td class="px-4 py-3">{{ record.nombres }}</td>
                    <td class="px-4 py-3">{{ record.apellidos }}</td>
                    <td class="px-4 py-3">{{ record.registro }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
