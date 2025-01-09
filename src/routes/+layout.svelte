<script lang="ts">
	let { children } = $props();
</script>
<div class="h-screen flex flex-col bg-gray-100">
	<nav>
		<a href="/">Home</a>
		<a href="/measurement-classification">Measurment Classification</a>
	</nav>
	
</div>
{@render children()}