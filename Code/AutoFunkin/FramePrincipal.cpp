///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "FramePrincipal.h"

///////////////////////////////////////////////////////////////////////////

FramePrincipal::FramePrincipal( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxSize( 300,200 ), wxSize( 600,400 ) );

	wxBoxSizer* bSizerPrincipal;
	bSizerPrincipal = new wxBoxSizer( wxVERTICAL );

	m_staticTextChooseMod = new wxStaticText( this, wxID_ANY, wxT("Please select your mod:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextChooseMod->Wrap( -1 );
	bSizerPrincipal->Add( m_staticTextChooseMod, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_comboBoxChoice = new wxComboBox( this, wxID_ANY, wxT("________________________________"), wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	bSizerPrincipal->Add( m_comboBoxChoice, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_buttonOK = new wxButton( this, wxID_ANY, wxT("OK"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizerPrincipal->Add( m_buttonOK, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	this->SetSizer( bSizerPrincipal );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_comboBoxChoice->Connect( wxEVT_COMMAND_COMBOBOX_SELECTED, wxCommandEventHandler( FramePrincipal::OnComboboxMod ), NULL, this );
	m_buttonOK->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FramePrincipal::OnOKButtonClick ), NULL, this );
}

FramePrincipal::~FramePrincipal()
{
	// Disconnect Events
	m_comboBoxChoice->Disconnect( wxEVT_COMMAND_COMBOBOX_SELECTED, wxCommandEventHandler( FramePrincipal::OnComboboxMod ), NULL, this );
	m_buttonOK->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FramePrincipal::OnOKButtonClick ), NULL, this );

}
