#include "EvtFramePrincipal.h"

EvtFramePrincipal::EvtFramePrincipal( wxWindow* parent )
:
FramePrincipal( parent ){
	std::cout<<"Please wait mods list fetch. May take up to 15 seconds."<<std::endl;
    std::vector<std::string> modNames = fetchModNames();

    if (modNames.empty()){
        std::cerr << "No mod names fetched. Check website structure or parsing logic." << std::endl;
    }

    std::sort(modNames.begin(), modNames.end());
    for (const auto& mod : modNames){
        m_comboBoxChoice->Append(mod);
    }
}

void EvtFramePrincipal::OnComboboxMod( wxCommandEvent& event ){
// TODO: Implement OnComboboxMod
}

void EvtFramePrincipal::OnOKButtonClick( wxCommandEvent& event ){
	std::string selectedMod = m_comboBoxChoice->GetValue().ToStdString();
	if (selectedMod == "________________________________" || selectedMod.empty()){
	}
	else {
		Close(true);
		Destroy();
	}
}

std::string EvtFramePrincipal::fetchHTMLContent(){
	#if __linux__
		system("curl -s https://fnfmod.online/popular-mods/>~/output.html");
		std::string output=system("echo $HOME>/dev/null") + "output.html";
		std::ifstream file(output);
		std::string htmlContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
		return htmlContent;
	#elif _WIN32
		system("curl -s https://fnfmod.online/popular-mods/ > %USERPROFILE%/output.html");
		std::string output=system("echo %USERPROFILE% > NUL") + "output.html";
		std::ifstream file(output);
		std::string htmlContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
		return htmlContent;
    #elif __APPLE__
        system("curl -s https://fnfmod.online/popular-mods/>~/output.html");
		std::string output=system("echo $HOME>/dev/null") + "output.html";
		std::ifstream file(output);
		std::string htmlContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
		return htmlContent;
	#else
		wxLog("Please use another ");
		exit();
	#endif
    
	//std::string output=system("echo $HOME>/dev/null") + "output.html";
    //std::ifstream file(output);
    //std::string htmlContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    //return htmlContent;
}

void search_for_links(GumboNode* node, std::vector<std::string>& modNames){
    if (node->type != GUMBO_NODE_ELEMENT) return;
    GumboAttribute* class_attr = gumbo_get_attribute(&node->v.element.attributes, "class");
    GumboAttribute* data_attr = gumbo_get_attribute(&node->v.element.attributes, "data-tippy-content");
    if (node->v.element.tag == GUMBO_TAG_A && class_attr && std::string(class_attr->value) == "personages__link" && data_attr){
        std::string content = data_attr->value;
        if (!content.empty()){
            modNames.push_back(content);
        }
    }

    GumboVector* children = &node->v.element.children;
    for (unsigned int i = 0; i < children->length; ++i) {
        search_for_links(static_cast<GumboNode*>(children->data[i]), modNames);
    }
}

std::vector<std::string> EvtFramePrincipal::fetchModNames(){
    std::string htmlContent = fetchHTMLContent();
    GumboOutput* output = gumbo_parse(htmlContent.c_str());
    std::vector<std::string> modNames;
    search_for_links(output->root, modNames);
    gumbo_destroy_output(&kGumboDefaultOptions, output);
    std::sort(modNames.begin(), modNames.end());
    return modNames;
}




