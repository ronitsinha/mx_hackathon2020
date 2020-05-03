window.onload = _ => {
	console.log('ready!')

	document.getElementById('requestadd').onclick = _ => {
		var food = document.getElementById('food').value;
		var qty = document.getElementById('qty').value;

		document.getElementById('requestorder').innerHTML += `<li>${food}: ${qty}</li>`;
	}
}