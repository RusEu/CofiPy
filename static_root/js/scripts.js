
$(document).ready(function(){/* off-canvas sidebar toggle */

	$('[data-toggle=offcanvas]').click(function() {
	  	$(this).toggleClass('visible-xs text-center');
	    $(this).find('i').toggleClass('glyphicon-chevron-right glyphicon-chevron-left');
	    $('.row-offcanvas').toggleClass('active');
	    $('#lg-menu').toggleClass('hidden-xs').toggleClass('visible-xs');
	    $('#xs-menu').toggleClass('visible-xs').toggleClass('hidden-xs');
	    $('#btnShow').toggle();
	});
	$('#text p').each(function() {
	    var str = $(this).text();
	    var search = str.search(" ")
	    if ( search == -1 || search > 30) {
		    var newStr = str.replace(/(.{30})/g, "$1\n");
			$(this).text(newStr);
		}
	});
	$(".exists a button").addClass("disabled")
	$(".exists a").attr("href","#")
});