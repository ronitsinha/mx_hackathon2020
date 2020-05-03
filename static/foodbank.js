orders = {}
var data=[{"formatted_address": "48 Monument Square, Concord, MA 01742, USA", "formatted_phone_number": "(978) 369-9200", "name": "Concord's Colonial Inn", "place_id": "ChIJ625sqTma44kRzlBradoLrgI", "website": "http://www.concordscolonialinn.com/"}, {"formatted_address": "79 Powers Rd, Westford, MA 01886, USA", "formatted_phone_number": "(978) 692-3033", "name": "Nashoba Valley Ski Area", "place_id": "ChIJFaQmI0WW44kRv3_NK5cH7y4", "website": "http://www.skinashoba.com/"}, {"formatted_address": "550 Winter St, Waltham, MA 02451, USA", "formatted_phone_number": "(781) 890-6767", "name": "The Grille at Hobbs Brook", "place_id": "ChIJF7XchLec44kRCWy44xF8lbw", "website": "http://embassysuites1.hilton.com/en_US/es/hotel/BOSWSES-Embassy-Suites-Boston-Waltham-Massachusetts/dining.do#1%20Thanks!"}, {"formatted_address": "72 Wayside Inn Rd, Sudbury, MA 01776, USA", "formatted_phone_number": "(978) 443-1776", "name": "Longfellow's Wayside Inn", "place_id": "ChIJgzpdraWO44kRU7dME-HnqK8", "website": "http://www.wayside.org/"}, {"formatted_address": "1 Worcester Rd, Framingham, MA 01701, USA", "formatted_phone_number": "(508) 879-7285", "name": "Olive Garden Italian Restaurant", "place_id": "ChIJTT4AOo-I44kRTFk635fA2Jc", "website": "https://www.olivegarden.com/locations/ma/framingham/framingham-shoppers-world-plaza/1511?cmpid=br:og_ag:ie_ch:loc_ca:OGGMB_dt:20190131_sn:gmb_gt:framingham-ma-1511_pl:locurl_rd:1393"}, {"formatted_address": "100 Wattaquadock Hill Rd, Bolton, MA 01740, USA", "formatted_phone_number": "(978) 779-5521", "name": "Nashoba Valley Winery, Distillery, Brewery and Restaurant", "place_id": "ChIJLTJ6pY7y44kRQy3ZOZLud5Y", "website": "http://nashobawinery.com/"}, {"formatted_address": "117 Massachusetts Turnpike West, Natick, MA 01760, USA", "formatted_phone_number": "(508) 655-2958", "name": "D'Angelo Grilled Sandwiches", "place_id": "ChIJExf-hBaG44kRb2elCGJSTH8", "website": "https://locations.dangelos.com/ma/natick/117-mass-turnpike-west.html"}, {"formatted_address": "743 Washington St, Newton, MA 02460, USA", "formatted_phone_number": "(617) 964-9200", "name": "Cabot's", "place_id": "ChIJY7PSsxR444kRXY071xWr-Qc", "website": "http://www.cabots.com/"}, {"formatted_address": "195 School St, Waltham, MA 02451, USA", "formatted_phone_number": "(781) 894-3339", "name": "The Chateau Restaurant Waltham", "place_id": "ChIJU0IfAdaC44kROuLO-7XxbM8", "website": "http://www.chateaurestaurant.com/"}, {"formatted_address": "1657 Worcester Rd, Framingham, MA 01701, USA", "formatted_phone_number": "(508) 879-7200", "name": "The Postern Grille", "place_id": "ChIJ95gJpCeK44kRcQE7J-ztSp8", "website": "http://www.posterngrille.com/"}, {"formatted_address": "100 District Ave, Burlington, MA 01803, USA", "formatted_phone_number": "(781) 272-9000", "name": "Tavern In the Square", "place_id": "ChIJFUszHDee44kR_fO1eK3W6zA", "website": "http://taverninthesquare.com/"}, {"formatted_address": "1 Worcester Rd, Framingham, MA 01701, USA", "formatted_phone_number": "(508) 875-2337", "name": "John Harvard's Brewery & Ale House", "place_id": "ChIJTT4AOo-I44kRv059bzLdKM4", "website": "http://johnharvards.net/"}, {"formatted_address": "100 Clinton St, Framingham, MA 01702, USA", "formatted_phone_number": "(508) 872-0900", "name": "Jack's Abby Craft Lagers", "place_id": "ChIJ2dmYFGuI44kRqJ3UUE0HbMw", "website": "http://jacksabby.com/"}, {"formatted_address": "94 Hartwell Ave, Lexington, MA 02421, USA", "formatted_phone_number": "(781) 861-9299", "name": "Waxy O'Connor's", "place_id": "ChIJMRl_Gp-e44kRb1N-E6uDaY8", "website": "https://m.facebook.com/waxyslexington/"}, {"formatted_address": "388 Moody St, Waltham, MA 02453, USA", "formatted_phone_number": "(781) 894-1805", "name": "Solea Restaurant and Tapas Bar", "place_id": "ChIJYyqk39iC44kR72vMGe5PA3Y", "website": "http://www.soleatapas.com/"}, {"formatted_address": "1391 Washington St, West Newton, MA 02465, USA", "formatted_phone_number": "(617) 340-2160", "name": "The Local Newton", "place_id": "ChIJUQQgIfqC44kRe6yq2fkrw-Q", "website": "http://www.liveeatlocal.com/newton"}, {"formatted_address": "107R Union St, Newton, MA 02459, USA", "formatted_phone_number": "(617) 964-6684", "name": "Union Street Restaurant and Bar", "place_id": "ChIJz9LegIJ444kRMJke8j-E-W0", "website": "http://unionst.com/"}, {"formatted_address": "49 Boylston St, Chestnut Hill, MA 02467, USA", "formatted_phone_number": "(617) 651-3406", "name": "Shake Shack", "place_id": "ChIJw-3qvpJ444kRK9qbwuxAGTE", "website": "http://www.shakeshack.com/"}, {"formatted_address": "475 Winter St, Waltham, MA 02451, USA", "formatted_phone_number": "(781) 684-0650", "name": "Bertucci's Italian Restaurant", "place_id": "ChIJryE0ksec44kROWzerIaLeHQ", "website": "https://www.bertuccis.com/?utm_source=google&utm_campaign=lgmb&utm_medium=organic&utm_content=local-listing"}, {"formatted_address": "1030 Main St #5, Waltham, MA 02451, USA", "formatted_phone_number": "(781) 899-4937", "name": "Chipotle Mexican Grill", "place_id": "ChIJAR1cDDCD44kRNPEaWdLfJ60", "website": "https://locations.chipotle.com/ma/waltham/1030-main-st?utm_source=google&utm_medium=yext&utm_campaign=yext_listings"}]

window.onload = _ => {
	console.log('ready!')

	console.log(data)
	console.log(document.getElementById('nearby'))

	document.getElementById('requestadd').onclick = _ => {
		var food = document.getElementById('food').value;
		var qty = document.getElementById('qty').value;

		document.getElementById('requestorder').innerHTML += `<li>${food}: ${qty}</li>`;
		orders[food] = parseInt(qty);
	}

	document.getElementById('placeorder').onclick = place_order;

	var nearby = document.getElementById('nearby')

	for (var i in data.length) {
		nearby.innerHTML += `<li><a=href="${data[i]['website']}">${data[i]['name']}</a></li>`;
	}
}


function place_order () {
	console.log('Order placed!');

	for (var key in orders) {
		console.log(`${key}: ${orders[key]}`);
	}

	$.post('/handle_name_search/restaurant', {
		js_data: JSON.stringify(orders)
	});
}