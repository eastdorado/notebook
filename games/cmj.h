#ifndef _CMJ_H 
#define _CMJ_H 
//============================================ 
//Author:Honghaier 
//Date:2006-12-20 
//QQ:285421210 
//============================================ 
#include <windows.h> 
#include <iostream> 
#include <vector> 
#include <algorithm> 
using namespace std; 
  
  
#define MJPAI_ZFB    0 //�У������� 
#define MJPAI_FENG    1 //�����ϱ��� 
#define MJPAI_WAN    2 //�� 
#define MJPAI_TIAO    3 //�� 
#define MJPAI_BING    4 //�� 
#define MJPAI_HUA    5 //�� 
  
#define MJPAI_GETPAI   true //���� 
#define MJPAI_PUTPAI   false //���� 
//�ڵ���Ϣ 
struct stPAI 
{ 
 int  m_Type;    //������ 
 int  m_Value;   //���� 
  
} 
; 
  
//����˳ 
struct stCHI      
{ 
 int  m_Type;    //������ 
 int  m_Value1;   //���� 
 int  m_Value2;   //���� 
 int  m_Value3;   //���� 
} 
; 
// m_Type  m_Value 
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-// 
// 0  | �� 1 ��2 ��            
//   | 
// 1  | �� 1 ��2 ��  ��         
//   | 
// 2  | һ�� ���� ���� ���� 
//   | 
// 3  | һ�� ���� ���� ����     
//   | 
// 4  | һ�� ���� ���� �ű� 
//   | 
// 5  | ��  ��  ��  ��  ��  ��  ÷  �� 
//   | 
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-// 
  
  
  
//������Ϣ 
struct stGoodInfo 
{ 
 char m_GoodName[100];   //�������� 
 int  m_GoodValue;    //���Ʒ��� 
} 
; 
//�� 
class CMJ 
{ 
 vector< int >  m_MyPAIVec[6];  //��������� 
 vector< int >  m_ChiPAIVec[6];  //�Ե������� 
 vector< int >  m_PengPAIVec[6]; //���������� 
 vector< int >  m_GangPAIVec[6]; //�ܵ������� 
  
 stPAI    m_LastPAI;   //�������� 
 stGoodInfo   m_GoodInfo;   //������Ϣ 
  
 bool    m_9LBD;    //�Ƿ������������� 
 bool    m_13Y;    //�Ƿ���ʮ���� 
 int     m_MKNum;   //������ 
 int     m_AKNum;   //������ 
 bool    m_4AK;    //�Ƿ������İ��� 
  
 vector< stCHI >  m_TempChiPAIVec; //�ԵĿ�ѡ��� 
 vector< stPAI >  m_TempPengPAIVec; //���Ŀ�ѡ��� 
 vector< stPAI >  m_TempGangPAIVec; //�ܵĿ�ѡ��� 
  
public: 
  
 //���� 
 CMJ(); 
 //���� 
 ~CMJ(); 
 //��ʼ�� 
 void   Init(); 
 //���� 
 bool   AddPai(int p_Type,int p_Value); 
 //ȡ�ö�Ӧ��������ǽ������ 
 int    GetPaiIndex(int p_Type,int p_Value); 
 //����(����Ϊ��Ӧ��������ǽ������) 
 bool   DelPai(int PaiIndex); 
 //ɾ���� 
 bool   DelPai(int p_Type,int p_Value); 
 //����� 
 void   CleanUp(); 
 //ȡ�ú�����Ϣ 
 stGoodInfo  *GetInfo(); 
 //����Ƿ���� 
 bool   CheckAllPai(bool GetOrPut); 
 //�����е��ƽ������ 
 void   PrintAllPai(); 
 //��һ���ƽ������ 
 void   PrintPai(int p_Type,int p_Value); 
 //���� 
 bool   CheckChiPai(int p_Type,int p_Value); 
 //���� 
 bool   DoChiPai(int p_iIndex,int p_Type,int p_Value); 
 //���� 
 bool   CheckPengPai(int p_Type,int p_Value); 
 //���� 
 bool   DoPengPai(int p_Type,int p_Value); 
 //���� 
 bool   CheckGangPai(int p_Type,int p_Value); 
 //���� 
 bool   DoGangPai(int p_Type,int p_Value); 
 //�ԿɳԵ���Ͻ������ 
 void   PrintChiChosePai(); 
 //�Կ�������Ͻ������ 
 void   PrintPengChosePai(); 
 //�Կɸܵ���Ͻ������ 
 void   PrintGangChosePai(); 
 //ȡ�ó�������� 
 UINT   GetChiChoseNum(); 
  
private: 
  
 //����Ƿ���ƣ��ţ� 
 bool CheckAAPai(int iValue1,int iValue2); 
 //����Ƿ������� 
 bool CheckABCPai(int iValue1,int iValue2,int iValu3); 
 //����Ƿ������� 
 bool CheckAAAPai(int iValue1,int iValue2,int iValu3); 
 //����Ƿ������� 
 bool CheckAAAAPai(int iValue1,int iValue2,int iValu3,int iValue4); 
 //����Ƿ������� 
 bool CheckAABBCCPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6); 
 //����Ƿ�������ѹ 
 bool CheckAAABBBCCCPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9); 
 //����Ƿ������� 
 bool CheckAAAABBBBCCCCPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12); 
 //����Ƿ������� 
 bool CheckAABBCCDDEEFFPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12); 
 //�����Ƽ��=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
   
 //����Ƿ���ƣ��ţ� 
 bool Check5Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5); 
 //����Ƿ���ƣ��ţ� 
 bool Check8Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8); 
 //����Ƿ���ƣ��ţ� 
 bool Check11Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11); 
 //����Ƿ���ƣ��ţ� 
 bool Check14Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12,int iValue13,int iValue14); 
  
 //�������Ƽ��-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
   
 //����Ƿ���ƣ��ţ� 
 bool Check3Pai(int iValue1,int iValue2,int iValue3); 
 //����Ƿ���ƣ��ţ� 
 bool Check6Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6); 
 //����Ƿ���ƣ��ţ� 
 bool Check9Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9); 
 //����Ƿ���ƣ��ţ� 
 bool Check12Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12); 
   
  
private:  
 //�����ж� 
  
 //����Ƿ������ϲ 
 bool CheckD4X_HU(); 
 //�����Ƿ������Ԫ 
 bool CheckD3Y_HU(); 
 //����Ƿ����һɫ 
 bool CheckL1S_HU(); 
 //����Ƿ���������� 
 bool Check9LBD_HU(); 
 //����Ƿ���ĸ� 
 bool Check4Gang_HU(); 
 //����Ƿ�����߶� 
 bool CheckL7D_HU(); 
 //����Ƿ��ʮ���� 
 bool Chekc13Y_HU(); 
 //����Ƿ�����۾� 
 bool CheckQY9_HU(); 
 //����Ƿ��С��ϲ 
 bool CheckX4X_HU(); 
 //����Ƿ��С��Ԫ 
 bool CheckX3Y_HU(); 
 //����Ƿ����һɫ 
 bool CheckZ1S_HU(); 
 //����Ƿ��İ��� 
 bool Check4AK_HU(); 
 //����Ƿ�һɫ˫���� 
 bool Check1S2LH_HU(); 
 //����Ƿ�һɫ��ͬ˳ 
 bool Check1S4TS_HU(); 
 //����Ƿ�һɫ�Ľڸߣ� 
 bool Check1S4JG_HU(); 
 //����Ƿ�һɫ�Ĳ��ߣ� 
 bool Check1S4BG_HU(); 
 //����Ƿ����� 
 bool Check3Gang_HU(); 
 //����Ƿ���۾� 
 bool CheckHY9_HU(); 
 //����Ƿ��߶� 
 bool Check7D_HU(); 
 //����Ƿ����ǲ��� 
 bool Check7XBK_HU(); 
 //����Ƿ�ȫ˫�̣� 
 bool CheckQSK_HU(); 
 //��һɫ 
 bool CheckQ1S_HU(); 
 //����Ƿ�һɫ��ͬ˳ 
 bool Check1S3TS_HU(); 
 //����Ƿ�һɫ���ڸ� 
 bool Check1S3JG_HU(); 
 //����Ƿ�ȫ�� 
 bool CheckQD_HU(); 
 //����Ƿ�ȫ�� 
 bool CheckQZ_HU(); 
 //����Ƿ�ȫС 
 bool CheckQX_HU(); 
 //����Ƿ����� 
 bool CheckQL_HU(); 
 //����Ƿ���ɫ˫���� 
 bool Check3S2LH_HU(); 
 //����Ƿ�һɫ������ 
 bool Check1S3BG_HU(); 
 //ȫ���� 
 bool CheckQD5_HU(); 
 //��ͬ�� 
 bool Check3TK_HU(); 
 //������ 
 bool Check3AK_HU(); 
 //������ 
 bool CheckDDJ_HU(); 
 //���� 
 bool CheckHU(); 
private: 
 //�����ж� 
  
 //����Ƿ����������� 
 bool Check9LBD_TING(); 
 //����Ƿ���ʮ���� 
 bool Check13Y_TING(); 
 //����Ƿ����İ��� 
 bool Check4AK_TING(); 
 //����Ƿ����� 
 bool CheckTING(); 
  
} 
; 
  
#endif 