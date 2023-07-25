$(document).ready(function(){
    var classes = $("#template").html();
    Mustache.parse(classes);
    var classInfo = Mustache.render(classes, classNames);
    $("#template").html(classInfo);
})

var classNames = {
    classOne: "Biology",
    descriptionOne: "An introduction to the study of isLegacyAndroidBuildOutputFile.",
    classTwo: "Principles of Biomedical Science",
    descriptionTwo: "An introductory biomedical science course covering forenisics, medical treatments, and emergency medicine.",
    classThree: "Principles of Biomedical Science",
    descriptionThree: "An introductory biomedical science course covering forenisics, medical treatments, and emergency medicine.",
    classFour: "Forensics",
    descriptionFour: "An advanced course covering the essentials of forensic laboratory science.",
    classFive: "Medical Interventions",
    descriptionFive: "An advanced biomedical course covering advanced medical testing and diagnostic techniques.",
    classSix: "Medical Interventions",
    descriptionSix: "An advanced biomedical course covering advanced medical testing and diagnostic techniques."
};