Action()
{
	//新增会员
	web_reg_save_param_json(
		"ParamName=add_customer_checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//新增会员事务
	lr_start_transaction("add_customer");

	//请求
	web_submit_data("add_customer",
		"Action=https://snailpet.com/v2/Members/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=addr", "Value=", ENDITEM,
		"Name=cardNumber", "Value=", ENDITEM,
		"Name=is_open_upgrade", "Value=1", ENDITEM,
		"Name=is_spending_msg", "Value=1", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=member_tags", "Value=", ENDITEM,
		"Name=name", "Value={name}", ENDITEM,
		"Name=pets", "Value=[]", ENDITEM,
		"Name=phone", "Value={phone}", ENDITEM,	
		"Name=sex", "Value=", ENDITEM,
		"Name=shop_id", "Value=17531", ENDITEM,
		"Name=shopId", "Value=17531", ENDITEM,
		"Name=spare_phone", "Value=", ENDITEM,			
		LAST);
	
	//断言
	if (atoi(lr_eval_string("{error}"))==atoi(lr_eval_string("{add_customer_checkpoint}"))){
 		lr_end_transaction("add_customer", LR_PASS);
	}else{
		lr_end_transaction("add_customer", LR_FAIL);
	}
	
	//新增商品
	web_reg_save_param_json(
		"ParamName=add_product_checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//新增商品事务
	lr_start_transaction("add_product");

	//请求
	web_submit_data("add_product",
		"Action=https://snailpet.com/v2/Product/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=shopId", "Value=17531", ENDITEM,
		"Name=productId", "Value=0", ENDITEM,
		"Name=barCode", "Value={barcode}", ENDITEM,
		"Name=isServer", "Value=0", ENDITEM,
		"Name=name", "Value={pname}", ENDITEM,
		"Name=categoryId", "Value=839452", ENDITEM,
		"Name=inPrice", "Value={inPrice}", ENDITEM,
		"Name=outPrice", "Value={outPrice}", ENDITEM,
		"Name=percentage", "Value=0", ENDITEM,	
		"Name=stocks", "Value={stocks}", ENDITEM,
		"Name=notice_stocks", "Value=1", ENDITEM,
		"Name=weight", "Value=0", ENDITEM,
		"Name=logo_images", "Value=", ENDITEM,
		"Name=detail_images", "Value=", ENDITEM,
		"Name=shelf_life", "Value=90", ENDITEM,
		"Name=production_time", "Value=1583942400", ENDITEM,
		"Name=brand_name", "Value=", ENDITEM,
		"Name=add_brand_category_id", "Value=15", ENDITEM,		
		"Name=version", "Value=1", ENDITEM,
		"Name=shop_id", "Value=17531", ENDITEM,		
		LAST);
	
	//断言
	if (atoi(lr_eval_string("{error}"))==atoi(lr_eval_string("{add_product_checkpoint}"))){
 		lr_end_transaction("add_product", LR_PASS);
	}else{
		lr_end_transaction("add_product", LR_FAIL);
	}
	
	//商品入库
	web_reg_save_param_json(
		"ParamName=input_product_checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//商品入库事务
	lr_start_transaction("input_product");

	//请求
	web_submit_data("input_product",
		"Action=https://snailpet.com/v2/product/update/stocks",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=exp_time", "Value=1598457600", ENDITEM,
		"Name=inPrice", "Value={inPrice}", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=number", "Value={inumber}", ENDITEM,
		"Name=productId", "Value=2133565", ENDITEM,
		"Name=production_time", "Value=1585238400", ENDITEM,
		"Name=shelf_life", "Value=153", ENDITEM,
		"Name=shop_id", "Value=17531", ENDITEM,
		"Name=shopId", "Value=17531", ENDITEM,	
		LAST);
	
	//断言
	if (atoi(lr_eval_string("{error}"))==atoi(lr_eval_string("{input_product_checkpoint}"))){
 		lr_end_transaction("input_product", LR_PASS);
	}else{
		lr_end_transaction("input_product", LR_FAIL);
	}
	
	//商品出库
	web_reg_save_param_json(
		"ParamName=checkout_product_checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//商品出库事务
	lr_start_transaction("checkout_product");

	//请求
	web_submit_data("update_product",
		"Action=https://snailpet.com/v2/product/update/stocks",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=exp_time", "Value=1598457600", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=number", "Value={cnumber}", ENDITEM,
		"Name=out_of_price", "Value={outPrice}", ENDITEM,
		"Name=productId", "Value=2133565", ENDITEM,
		"Name=production_time", "Value=1585238400", ENDITEM,
		"Name=shelf_life", "Value=0", ENDITEM,
		"Name=shop_id", "Value=17531", ENDITEM,
		"Name=shopId", "Value=17531", ENDITEM,	
		LAST);
	
	//断言
	if (atoi(lr_eval_string("{error}"))==atoi(lr_eval_string("{checkout_product_checkpoint}"))){
 		lr_end_transaction("checkout_product", LR_PASS);
	}else{
		lr_end_transaction("checkout_product", LR_FAIL);
	}
	
	
	//添加会员卡
	web_reg_save_param_json(
		"ParamName=add_VipCard_checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//添加事务
	lr_start_transaction("add_VipCard");

	//请求
	web_submit_data("add_VipCard",
		"Action=https://snailpet.com/v2/Shop/setMemberLevel",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=background", "Value=0", ENDITEM,
		"Name=discount", "Value=10", ENDITEM,
		"Name=discount_for_combination", "Value=10", ENDITEM,
		"Name=discountForService", "Value=10", ENDITEM,
		"Name=enablePlus", "Value=1", ENDITEM,
		"Name=minPrice", "Value={minPrice}", ENDITEM,
		"Name=name", "Value={name}", ENDITEM,
		"Name=shop_id", "Value=17531", ENDITEM,
		"Name=shopId", "Value=17531", ENDITEM,	
		LAST);
	
	//断言
	if (atoi(lr_eval_string("{error}"))==atoi(lr_eval_string("{add_VipCard_checkpoint}"))){
 		lr_end_transaction("add_VipCard", LR_PASS);
	}else{
		lr_end_transaction("add_VipCard", LR_FAIL);
	}
	
	return 0;
}
