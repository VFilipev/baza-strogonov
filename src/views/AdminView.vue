<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Admin</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" href="#" :to="{ name: 'order' }">
                            Заказы
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" href="" :to="{ name: 'sauna' }">
                            Баня
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" href="" :to="{ name: 'plan' }">
                            Разнарядка
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" href="" :to="{ name: 'registry' }">
                            Реестр
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <router-view />
</template>

<script setup>

</script>

<style scoped>
.router-link-active{
    color: #000;
    font-weight: 500;
}
</style>