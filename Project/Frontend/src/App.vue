
<template>
  <div class="Contain">

    <div class="Topbar">
      <div class="column left">
        <h1>Game Energy | Computer Electricity Tracker</h1>
      </div>
    </div>


    <div class="desktop-1-1">

 
      <div class="rectangle-1-2"></div>


      <p class="text-3">
        <span class="text-white">
          {{ stats.total_kwh?.toFixed(4) || "…" }} kWh
        </span>
      </p>
      <p class="text-7">
        <span class="text-white">
          Avg CPU Usage: {{ stats.cpu_percent?.toFixed(1) || "…" }}%
        </span>
      </p>

 
      <p class="text-8">
        <span class="text-white">
          Avg GPU Usage: {{ stats.gpu_percent?.toFixed(1) || "…" }}%
        </span>
      </p>


      <p class="text-9">
        <span class="text-white"></span>
      </p>

      <div class="rectangle-6-10"></div>
      <div class="rectangle-7-11"></div>

      <p class="text-12">
        <span class="text-white">GOAL:</span>
      </p>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const stats = ref({})

async function fetchStats() {
  try {
    const res = await axios.get("http://localhost:8000/stats/latest")
    stats.value = res.data || {}
  } catch (err) {
    console.error("Failed to fetch stats:", err)
  }
}

onMounted(() => {
  fetchStats()
  setInterval(fetchStats, 3000)
})
</script>

<style scoped>
html, body {
  padding: 0;
  background-color: #1c1f27;
}
.Contain {
  background-color: #1c1f27;
  min-height: 100vh;
  width: 100vw; 
  overflow-x: hidden;
}
@font-face {
  font-family: 'NATS';
  src: url('@/assets/fonts/nats.woff2') format('woff2'),
       url('@/assets/fonts/nats.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

:root {
  --font-family-inter: 'Inter', sans-serif;
  --font-family-nats: 'NATS', sans-serif;
  color: #FFFFFF;
}

.text-white {
  color: #FFFFFF;
}

/* RESET */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}


.desktop-1-1 {
  position: relative;
  width: 1440px;
  height: 1024px;
  background: #303848; 
  overflow: hidden;
  margin: 0 auto;
}


.rectangle-1-2 {
  position: absolute;
  left: 80px;
  top: 120px;
  width: 600px;
  height: 200px;
  background: rgba(48, 56, 72, 1);
  border-radius: 8px;
}

.text-3 {
  position: absolute;
  left: 120px;
  top: 150px;
  font-family: var(--font-family-inter);
  font-weight: 700;
  font-size: 64px;
  color: #FFFFFF;
}

.rectangle-2-4 {
  position: absolute;
  left: 80px;
  top: 380px;
  width: 300px;
  height: 80px;
  background: rgba(36, 42, 53, 1);
  border-radius: 29px;
}

.rectangle-3-5 {
  position: absolute;
  left: 420px;
  top: 380px;
  width: 300px;
  height: 80px;
  background: rgba(76, 87, 113, 1);
}

.rectangle-5-6 {
  position: absolute;
  left: 760px;
  top: 380px;
  width: 300px;
  height: 80px;
  background: rgba(76, 87, 113, 1);
}

.text-7 {
  position: absolute;
  left: 90px;
  top: 480px;
  font-family: var(--font-family-nats);
  font-size: 24px;
  color:#FFFFFF;
}

.text-8 {
  position: absolute;
  left: 90px;
  top: 520px;
  font-family: var(--font-family-nats);
  font-size: 24px;
  color: #FFFFFF;
}

.text-9 {
  position: absolute;
  left: 90px;
  top: 560px;
  font-family: var(--font-family-nats);
  font-size: 24px;
  color: #FFFFFF;
}

.rectangle-6-10 {
  position: absolute;
  left: 90px;
  top: 600px;
  width: 500px;
  height: 20px;
  background: rgba(255, 255, 255, 0.26);
}

.rectangle-7-11 {
  position: absolute;
  left: 90px;
  top: 600px;
  width: 250px;
  height: 20px;
  background: rgba(255, 255, 255, 1);
}

.text-12 {
  position: absolute;
  left: 90px;
  top: 640px;
  font-family: var(--font-family-nats);
  font-size: 24px;
  color: #FFFFFF;
}


.Contain {
  background-color: #242832;
  min-height: 100vh;
}

.Topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #1c1f27;
  color: white;
  padding: 16px 32px;
}

.Topbar h1 {
  font-size: 22px;
  font-family: var(--font-family-inter);
}

.bar {
  display: flex;
  gap: 24px;
  background-color: #2c303a;
  padding: 10px 32px;
}

.bar a {
  color: white;
  text-decoration: none;
}

.bar a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .desktop-1-1 {
    transform: scale(0.7);
    transform-origin: top left;
  }
}
</style>
