AccountMembershipActions = {

	removeOverlays : function() {
		$('#new_member_button').show();
		$('.popup_wrapper').css("position", "static");
		$('.removable').remove();
		$('.hideable').hide();
		$(document).off("keydown", AccountMembershipActions.keyCancel);
	},
	showHeaderActionsOverlay : function() {
		// if (AccountMembershipActions.addOverlayTemplate == null) {
		// AccountMembershipActions.addOverlayTemplate =
		// $('add_overlay_container').innerHTML;
		// }
		// AccountMembershipActions.removeOverlays();
		// var header_actions_link = $('.header_actions a').first();
		// var headerActions = $('.header_actions').first();
		// headerActions.setStyle('position:relative;');
		// header_actions_link.hide();
		// $('add_overlay_container').innerHTML =
		// AccountMembershipActions.addOverlayTemplate;
		$('#add_overlay_container').show();
		$('#add_member_overlay').show();
		$('#members_for_lookup').focus();
		$(document).keydown(AccountMembershipActions.keyCancel);
	},

	keyCancel : function(event) {
		if ((event.keyCode || event.charCode) == Event.KEY_ESC) {
			AccountMembershipActions.removeOverlays();
		}
	},
};