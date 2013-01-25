
function remove_contenttype_model_selectbox_empty_choices(form_id, contenttype_field) {
    type_field_id = "#id_" + contenttype_field + "_type";
    $(form_id + " " + type_field_id).find("option").each(function() {
        choices_field_id = "#id_" + contenttype_field + "_id_" + $(this).val();
        $(form_id + " " + choices_field_id).children(":first").remove();
    });
}

function change_contenttype_selectbox_choices(form_id, contenttype_field) {
    type_field_id = "#id_" + contenttype_field + "_type";
    id_field_id = "#id_" + contenttype_field + "_id";
    choices_field_id = "#id_" + contenttype_field + "_id_" + $(form_id + " " + type_field_id).val();

    $(form_id + " " + id_field_id).html($(form_id + " " + choices_field_id).html());
}