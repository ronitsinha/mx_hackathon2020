orders = {}

window.onload = _ => {
	console.log('ready!')

	document.getElementById('requestadd').onclick = _ => {
		var food = document.getElementById('food').value;
		var qty = document.getElementById('qty').value;

		document.getElementById('requestorder').innerHTML += `<li>${food}: ${qty}</li>`;
		orders[food] = parseInt(qty);
	}

	document.getElementById('placeorder').onclick = place_order;
}


function place_order () {
	console.log('Order placed!');

	for (var key in orders) {
		console.log(`${key}: ${orders[key]}`);
	}

	$.post('/handle_foodbank_request', {
		js_data: JSON.stringify(orders)
	});
}