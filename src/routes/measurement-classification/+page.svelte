<script lang="ts">
  let sepal_length = '';
  let sepal_width = '';
  let pedal_length = '';
  let pedal_width = '';
  let prediction = '';
  let errorMessage = '';

  async function handleSubmit(event: Event): Promise<void> {
    event.preventDefault()

    const data = {
      inputs: [
      parseFloat(sepal_length),
      parseFloat(sepal_width),
      parseFloat(pedal_length),
      parseFloat(pedal_width)
    ]
  }
  try {
    //send the data to the flask server
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 
        'content-type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if(!response.ok){
      throw new Error("Failed to fetch data")
    }

    const result = await response.json();
    console.log('API Response:', result);
    prediction = result.prediction;

  } catch (error) {
    if (error instanceof Error) {
        errorMessage = error.message;
      } else {
        errorMessage = 'An unknown error occurred.';
      }
      console.error('Error:', errorMessage); // Debugging: Log errors
    }
}
</script>

<form on:submit={handleSubmit}>
  <div class="h-screen flex flex-col items-center justify-center bg-gray-800">
    <h1 class="text-l font-bold text-gray-800">Measurement Classification</h1>
    <input type="text" bind:value={sepal_length} placeholder=sepal_length/>
    <input type="text" bind:value={sepal_width} placeholder=sepal_width/>
    <input type="text" bind:value={pedal_length} placeholder="pedal_length"/>
    <input type="text" bind:value={pedal_width} placeholder="pedal_width"/>
    <button>Enter</button>
  </div>
</form>

{#if prediction}
  <div class="text-white">
    <h2>Prediction: {prediction}</h2>
  </div>
{/if}