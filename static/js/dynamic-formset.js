    $(document).ready(function() {
        // Add button click event
        bindAddRowButtonClick('#add-row', '.remove-row-btn');

        function bindAddRowButtonClick(addButtonSelector, removeButtonSelector) {
            $(addButtonSelector).click(function() {
                addRow(addButtonSelector, removeButtonSelector);
                bindRemoveRowButtonClick(removeButtonSelector); // Re-bind click event after adding row
            });
        }

        function addRow(addButtonSelector, removeButtonSelector) {
            // Clone the last form container
            const lastFormContainer = $(removeButtonSelector).closest('.form-container');
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

        function bindRemoveRowButtonClick(removeButtonSelector) {
            $(removeButtonSelector).off('click').click(function() { // Use .off('click') to remove previous event bindings
                $(this).closest('.form-container').remove();
                updateFormElementIndices(); // Update form element indices after removing row
                updateTotalForms(); // Update total form count
            });
        }

        function updateFormElementIndices() {
            const prefix = 'book_set'; // Update with your formset prefix

            $('.form-container').each(function(index, container) {
                $(container).find(':input').each(function() {
                    const name = $(this).attr('name');
                    if (name) { // Check if the input field has a name attribute
                        const parts = name.split('-');
                        const newName = `${parts[0]}-${index}-${parts.slice(2).join('-')}`;
                        $(this).attr('name', newName);
                        $(this).attr('id', `id_${newName}`); // Update the id as well if necessary
                    }
                });
            });
        }

        function updateTotalForms() {
            const formPrefix = 'book_set'; // Update with your formset prefix
            const totalFormsInput = $('#id_' + formPrefix + '-TOTAL_FORMS');
            const newTotalForms = $('.form-container').length;
            totalFormsInput.val(newTotalForms);
        }

        // Initial binding
        bindRemoveRowButtonClick('.remove-row-btn');
    });
