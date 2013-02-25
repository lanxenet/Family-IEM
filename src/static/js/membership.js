$.extend( $.fn.popover.Constructor.prototype,{
    getPosition: function (inside) {
        console.log("getPosition");
        return $.extend({},
            (inside
                ?
                {top: 0, left: 0}
                :
                {top: this.$element.offset().top, left: this.$element.offset().left-150}
            ),
            {
            width: this.$element[0].offsetWidth,
            height: this.$element[0].offsetHeight
            }
        )
    }
});

$('#add-member').popover({
    html: true,
    trigger: 'click',
    container: 'body',
    title: function() {
        return $("#add-member-form-title").html();
    },
    content: function() {
        return $("#add-member-form").html();
    }
});

AccountMembershipActions = {
    showHeaderActionsOverlay : function() {
        $('#add-member').popover('show');
        $(document).keydown(AccountMembershipActions.keyCancel);
    },

    removeOverlays : function() {
        $('#add-member').popover('hide');
        $(document).off("keydown", AccountMembershipActions.keyCancel);
    },

    keyCancel : function(event) {
        if ((event.keyCode || event.charCode) == Event.KEY_ESC) {
            AccountMembershipActions.removeOverlays();
        }
    },
};
