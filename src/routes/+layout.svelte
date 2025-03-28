<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>
<div class="">
	<nav>
		<a href="/">Home</a>
		<a href="/measurement-classification">Measurment Classification</a>
	</nav>
	
</div>
{@render children()}