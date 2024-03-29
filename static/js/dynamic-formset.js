$(document).ready(function() {
    // Add button click event
    bindAddRowButtonClick('#add-row', '.remove-row-btn');

    function bindAddRowButtonClick(addButtonSelector, removeButtonSelector) {
        $(addButtonSelector).click(function() {
            addRow();
            bindRemoveRowButtonClick(removeButtonSelector); // Re-bind click event after adding row
        });
    }

    function addRow() {
        // Clone the last form container
        const lastFormContainer = $('.form-container').last();
        const newFormContainer = lastFormContainer.clone();

        // Clear input values in the cloned form
        newFormContainer.find('input').val('');
        newFormContainer.find('select').val('');
        newFormContainer.find('input[type="hidden"]').remove();

        // Append the cloned form after the last one
        lastFormContainer.after(newFormContainer);

        // Update indices and total forms after adding a new row
        updateFormElementIndices();
        updateTotalForms();
    }

    function updateFormElementIndices() {
        const prefix = 'book'; // Get the prefix from views and use it here

        $('.form-container').each(function(index, container) {
            $(container).find(':input').each(function() {
                const name = $(this).attr('name');
                if (name) { // Check if the input field has a name attribute
                    const parts = name.split('-');
                    const newName = `${prefix}-${index}-${parts.slice(2).join('-')}`;
                    $(this).attr('name', newName);
                    $(this).attr('id', `id_${newName}`); // Update the id as well if necessary
                }
            });
        });
    }

    function updateTotalForms() {
        const formPrefix = 'book'; // Get the prefix from views and use it here
        const totalFormsInput = $('#id_' + formPrefix + '-TOTAL_FORMS');
        const newTotalForms = $('.form-container').length;
        totalFormsInput.val(newTotalForms);
    }

    function bindRemoveRowButtonClick(removeButtonSelector) {
        $(removeButtonSelector).off('click').click(function() { // Use .off('click') to remove previous event bindings
            $(this).closest('.form-container').remove();
            updateFormElementIndices(); // Update form element indices after removing row
            updateTotalForms(); // Update total form count
        });
    }

    // Initial binding
    bindRemoveRowButtonClick('.remove-row-btn');
});