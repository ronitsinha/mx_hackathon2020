offers = {}

window.onload = _ => {
	console.log('ready!')

	document.getElementById('requestadd').onclick = _ => {
		var food = document.getElementById('food').value;
		var qty = document.getElementById('qty').value;

		document.getElementById('requestorder').innerHTML += `<li>${food}: ${qty}</li>`;
		offers[food] = parseInt(qty);
	}

	document.getElementById('placeorder').onclick = make_offer;
}


function make_offer () {
	console.log('Offer made!');

	for (var key in offers) {
		console.log(`${key}: ${offers[key]}`);
	}

	$.post('/handle_restaurant_offer', {
		js_data: JSON.stringify(offers)
	});
}