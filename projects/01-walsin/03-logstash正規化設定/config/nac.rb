def register(params)
    # @drop_percentage = params["percentage"]
end

# the filter method receives an event and must return a list of events.
# Dropping an event means not including it in the return array,
# while creating new ones only requires you to add a new instance of
# LogStash::Event to the returned array
def filter(event)
    splitter = "Label: "
    if !event.get("nac_label_message").nil?
        if event.get("nac_label_message").include? splitter
            dataArr = event.get("nac_label_message").split(splitter).reject { |c| c.empty? }
            event.set("label_arr", dataArr)
            # p event.get("nac_label_message").split(", ")
        else
            event.set("label_arr", [event.get("nac_label_message")])
            # p [event.get("nac_label_message")]
        end
        # p event.get("nac_label_message")
    end


    return [event]
end
