#ifndef __EvtFramePrincipal__
#define __EvtFramePrincipal__

/**
@file
Subclass of FramePrincipal, which is generated by wxFormBuilder.
*/

#include "FramePrincipal.h"

//// end generated include
#include <fstream>
#include <gumbo.h>
#include <wx/log.h>
/** Implementing FramePrincipal */
class EvtFramePrincipal : public FramePrincipal
{
	protected:
		// Handlers for FramePrincipal events.
		void OnComboboxMod( wxCommandEvent& event );
		void OnOKButtonClick( wxCommandEvent& event );
	public:
		/** Constructor */
		EvtFramePrincipal( wxWindow* parent );
	//// end generated class members
	private:
        std::vector<std::string> fetchModNames();  // Declaration
        std::string fetchHTMLContent();           // Declaration

};

#endif // __EvtFramePrincipal__