function getLastInput() {
		table  = $('#new_question_answers_table')[0];

}

function addOption() {
		if (!this.questionCount) {
				this.questionCount = 1;
		}

		// var formTable  = $('#new_question_answers_table>tbody')[0];

		// One of the elements is the question text
		// var this.questionCount = formTable.getElementsByTagName('input').length - 1;

		// var newOption = document.getElementById('id_question1').cloneNode(true);
		// newOption.getElementsByTagName('td')[0].innerText =
		// 		'Option ' + (this.questionCount + 1).toString();
		// var newOptionInput = newOption.getElementsByTagName('input')[0];
		// newOptionInput.type = 'text';
		// newOptionInput.name = 'option' + (this.questionCount + 1).toString();
		// newOptionInput.id = "id_question" + (this.questionCount + 1).toString();
		// newOptionInput.value = "";

		// ++this.questionCount;
		// formTable.appendChild(newOption);

		var newOption = $(".answer-template").children()[0].cloneNode(true);

		$(newOption).find("label")[0].attributes["for"] = 'answerText' + this.questionCount.toString();
		$(newOption).find("input")[0].attributes["id"] = 'answerText' + this.questionCount.toString();

		++this.questionCount;
		$("#newQuestion")[0].appendChild(newOption);

		// $(newOption).find("label:first")[0].attr('for', 'answerText' + this.questionCount.toString());
		// $(newOption).find("[id=anwerText]")[0].id = "answerText" + this.questionCount.toString();
}

function isLastInput(obj) {

		if (obj.siblings().length == obj.index()) {
				return true;
		}

		return false;
}

function handleInputChange(obj) {

		// var form-group = $(obj).parent(".form-group");

		if (obj.value && isLastInput(form-group)) {
				addOption();
		}
		else if (!isLastInput(form-group) && !obj.value) {
				// We should remove the next option, if it is not empty
				$(form-group.parent().children()[form-group.index()-1]).find("input")[0].focus();
				form-group.remove();
		}

}

function getNextTr(obj) {
		return parentTr.parent().children()[parentTr.index()+1];
}
